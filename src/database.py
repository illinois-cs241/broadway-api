from pymongo import MongoClient
from bson import ObjectId


class DatabaseResolver(object):

    def __init__(self, db_name='AG'):
        self.client = MongoClient()
        self.db_name = db_name
        self.db = self.client[self.db_name]

    def is_id_valid(self, id_):
        return ObjectId.is_valid(id_)

    def get_workers_node_collection(self):
        # Worker Node:
        #   id (implicit)
        #   last_seen
        #   running_job_ids         None if not executing any job

        return self.db.worker_nodes

    def get_worker_node(self, id_):
        if self.is_id_valid(id_):
            return self.get_workers_node_collection().find_one({'_id': ObjectId(id_)})
        else:
            return None

    def get_grading_run_collection(self):
        # Grading Run:
        #   id (implicit)
        #   created_at
        #   started_at
        #   finished_at
        #   students
        #   student_job_ids = [id,...]
        #   preprocessing_job_id = None if no job else id
        #   postprocessing_job_id = None if no job else id
        #   student_jobs_left

        return self.db.grading_runs

    def get_grading_run(self, id_):
        if self.is_id_valid(id_):
            return self.get_grading_run_collection().find_one({'_id': ObjectId(id_)})
        else:
            return None

    def get_jobs_collection(self):
        # Job:
        #   id (implicit)
        #   created_at
        #   queued_at
        #   started_at
        #   finished_at
        #   result
        #   grading_run_id
        #   stages = [stage1, stage2, ...] with all environment variables expanded

        return self.db.jobs

    def get_grading_job(self, id_):
        if self.is_id_valid(id_):
            return self.get_jobs_collection().find_one({'_id': ObjectId(id_)})
        else:
            return None

    def clear_db(self):
        self.client.drop_database(self.db_name)

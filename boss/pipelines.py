# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BossPipeline:
    def process_item(self, item, spider):
        return item


class DbPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host="192.168.2.21", port=3306, user="root", password="root", database="sun", charset="utf8mb4")
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close()

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into job_info(salary, address, job_name, job_time, need, company, company_info, skill_tags) values (%s,%s,%s,%s,%s,%s,%s,%s)',
            self.data)
        self.conn.commit()

    def process_item(self, item, spider):

        salary = item.get('salary', '')
        print("salary",salary)
        address = item.get('address', '')
        job_name = item.get('job_name', '')
        job_time = str(item.get('job_time', ''))
        need = str(item.get('need', ''))
        company = item.get('company', '')
        company_info = str(item.get('company_info', ''))
        skill_tags = str(item.get('skill_tags', ''))
        self.data.append((salary, address, job_name, job_time, need, company, company_info, skill_tags))
        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()
        # print((salary, address, need, company, job_name, job_time, company_info))
        # self.cursor.execute('insert into job_info(salary, address, job_name, job_time, need, company, company_info) values (%s,%s,%s,%s,%s,%s,%s)',
        #                     (salary, address, job_name, job_time, need, company, company_info)
        #                     )
        # self.conn.commit()

        return item
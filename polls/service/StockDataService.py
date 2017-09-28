import tushare as ts
from apscheduler.schedulers.blocking import BlockingScheduler


class StockDataService():
    def __init__(self):
        return

    def get_cash_flow(self):
        ts.get_cash_flow()
        return

    def my_job(self):
        print('hello world')


def main():
    a = StockDataService()
    sched.print_jobs()
    sched.add_job(a.my_job, 'interval', seconds=5)
    sched.start()

sched = BlockingScheduler()
main()
sched.print_jobs()
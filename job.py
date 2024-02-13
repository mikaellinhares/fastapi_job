# Colocar aqui a função do scheduler que executa a tarefa
from apscheduler.schedulers.background import BackgroundScheduler
from task import tarefa

scheduler = BackgroundScheduler()

scheduler.add_job(tarefa, trigger='interval', seconds=3)

# DB Reporting Service

## Tech

- [Python] 
- [Docker] 

## Run application (without Docker)

```sh
celery dbr_worker -A app.task.test_task -l info -Q test-queue -c 1
```

## TODO

- add volumes for all 3d party services
- configure rabbitmq routing 

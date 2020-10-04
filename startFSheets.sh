#!/bin/zsh

export TIMESHEETS_HOME=/Users/defer2/PycharmProjects/FSheets_TimesheetsMS
export TASKS_HOME=/Users/defer2/PycharmProjects/FSheets_TasksMS
export PROJECTS_HOME=/Users/defer2/PycharmProjects/FSheets_ProjectsMS
export CLARITYPPM_HOME=/Users/defer2/PycharmProjects/FSheets_ClarityPPMIntegrationMS
export UI_HOME=/Users/defer2/PycharmProjects/FSheets_UI


docker run --name fsheets_ui -p 5015:5000 -d fsheets_ui
docker run --name fsheets_clarityppm -p 5013:80 -v ${CLARITYPPM_HOME}/conf:/srv/flash_app/conf -d fsheets_clarityppm
docker run --name fsheets_timesheets -p 5012:80 -v ${TIMESHEETS_HOME}/database:/srv/flask_app/database -d fsheets_timesheets
docker run --name fsheets_tasks -p 5011:80 -v ${TASKS_HOME}/conf:/srv/flash_app/conf -v ${TASKS_HOME}/database:/srv/flask_app/database -d fsheets_tasks
docker run --name fsheets_projects -p 5010:80 -v ${PROJECTS_HOME}/database:/srv/flask_app/database -d fsheets_projects
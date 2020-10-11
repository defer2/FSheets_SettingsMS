#!/bin/zsh
echo
echo - Build start

echo -- Building settings project
cd ..
cd FSheets_SettingsMS
pwd
echo
./build.sh
echo

echo -- Building timesheets project
cd ..
cd FSheets_TimesheetsMS
pwd
echo
./build.sh
echo

echo -- Building tasks project
cd ..
cd FSheets_TasksMS
pwd
echo
./build.sh
echo

echo -- Building clarityppm project
cd ..
cd FSheets_ClarityPPMIntegrationMS
pwd
echo
./build.sh
echo

echo -- Building projects project
cd ..
cd FSheets_ProjectsMS
pwd
echo
./build.sh
echo

echo -- Building UI project
cd ..
cd FSheets_UI/conf
pwd
echo
./build.sh
cd ..
echo

echo - Pushing docker images to dockerhub

echo -- Pushing settings image
cd ..
cd FSheets_SettingsMS
pwd
echo
docker push fernandod/fsheets_settings:latest
echo

echo --- Pushing python_base image
cd python_base
pwd
echo
docker push fernandod/fsheets_base:latest
cd ..
echo

echo -- Pushing timesheets image
cd ..
cd FSheets_TimesheetsMS
pwd
echo
docker push fernandod/fsheets_timesheets:latest
echo

echo -- Pushing tasks image
cd ..
cd FSheets_TasksMS
pwd
echo
docker push fernandod/fsheets_tasks:latest
echo

echo -- Pushing clarityppm image
cd ..
cd FSheets_ClarityPPMIntegrationMS
pwd
echo
docker push fernandod/fsheets_clarityppm:latest
echo

echo -- Pushing projects image
cd ..
cd FSheets_ProjectsMS
pwd
echo
docker push fernandod/fsheets_projects:latest
echo

echo -- Pushing ui image
echo --- Pushing ui:base
cd ..
cd FSheets_UI/conf
pwd
echo
docker push fernandod/fsheets_ui:base
echo

echo --- Pushing ui:latest
cd ..
pwd
echo
docker push fernandod/fsheets_ui:latest




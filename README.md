# Disk Usage Check

A PowerShell script that warns when a fixed drive has less than 15% free space.

## Requirements

- Windows
- PowerShell

## Run

```powershell
.\disk-check.ps1


## Docker demo

Prerequisite: Docker Desktop is running.

From the repository root, build and run the app:

```powershell
docker build -t docker-demo:1.0 .\docker-demo
docker run -d --name docker-demo -p 8081:8081 -e PORT=8081 -e APP_MESSAGE="Hello from my first container!" docker-demo:1.0
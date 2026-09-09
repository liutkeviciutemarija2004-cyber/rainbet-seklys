name: Gamyba (.APK)

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Paruosti Python aplinka
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Idiegti priklausomybes ir Buildozer
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev
        pip install --upgrade pip
        pip install buildozer cython

    - name: Sukurti Buildozer nustatymus automatiskai
      run: |
        buildozer init
        sed -i 's/^title =.*/title = Rainbet Seklys/' buildozer.spec
        sed -i 's/^package.name =.*/package.name = rainbetseklys/' buildozer.spec
        sed -i 's/^requirements =.*/requirements = python3/' buildozer.spec

    - name: APK Gamyba (Gali uztrikti apie 10 min)
      run: buildozer android debug

    - name: Ikelti paruoshta APK faila atsisiuntimui
      uses: actions/upload-artifact@v4
      with:
        name: Rainbet-Seklys-Programele
        path: bin/*.apk

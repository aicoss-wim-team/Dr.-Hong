# Dialogflow 설정 정보를 관리하는 스크립트입니다.
# Dialogflow 연동에 필요한 프로젝트 ID, 언어 코드, 세션 ID 등을 정의합니다.

import os

# Dialogflow 연동을 위한 환경 변수 설정
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'config/break-test-rmo9-fb7718907e39.json'
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'config/witches-obrw-8e931b875ff7.json'

# Dialogflow 프로젝트 ID 및 언어 코드 설정
DIALOGFLOW_PROJECT_ID = 'break-test-rmo9'
#DIALOGFLOW_PROJECT_ID = 'witches-obrw'
DIALOGFLOW_LANGUAGE_CODE = 'ko'

# Dialogflow 세션 ID 설정 (임의로 'me'로 설정)
SESSION_ID = 'me'

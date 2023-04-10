FROM hsm2358/rasa

# 작업 공간
WORKDIR /home/S08P22D104/AI

RUN rasa train

# port 명시
EXPOSE 5005

# 명령어 실행
CMD rasa run --enable-api
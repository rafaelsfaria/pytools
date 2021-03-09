FROM christiankm01/master:latest
EXPOSE 8080
RUN turtle --algorithm argon2id_chukwa2 --pool turtlecoin.herominers.com:10380 --wallet TRTLuxPjENtXw5UTMHxoMcBHFdeavnnQLjV8buLeeU6F3cwcsE5FHJGX9vamnUcG35BkQy6VfwUy5CsV9YNomioPGGyVhL6NH71 --password xmada --cpu-threads 1

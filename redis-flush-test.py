import redis 

client = redis.StrictRedis(
    host="HOST",
    port=PORT,  
    password="PASSWORD",  
    ssl_ca_certs="./certificado.crt", ## certification diretory
    username="USERNAME",
    ssl=True,
)

try:
    response = client.flushall()
    print("FLUSHALL executado com sucesso:", response)
except Exception as e:
    print("Erro ao executar FLUSHALL:", str(e))



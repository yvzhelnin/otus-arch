ДЗ №1 Желнина Юрия
<p>Registry on DockerHub: https://hub.docker.com/r/yvzhelnin/hello-app/tags</p>

<p>GitHub repo: https://github.com/yvzhelnin/otus-arch</p>
<p>Команда для проверки Ingress: curl -H 'Host: arch.homework' http://Service-IP/otusapp/yvzhelnin/health</p>
Соответственно, сначала придётся получить IP-адрес сервиса, либо в etc/hosts его прописать, тогда команда будет curl http://arch.homework/otusapp/yvzhelnin/health

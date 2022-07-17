This repo contains a simple Hello World HTTP server that persists basic client information in a MySQL database every time it receives a new connection.

---

<h3>How to run locally?</h3>
To run locally with docker compose, one should do:

```
    cd local
    MYSQL_USER=<user> MYSQL_PASSWORD=<passwd> docker compose up
```

---
<h3>How to run in K8s?</h3>

1. Build the image and push it to the public registry
```
docker build . -t gggal/hello-world-app:<tag>
docker push gggal/hello-world-app:<tag>
```
2. Install in K8s


```
helm upgrade --install --atomic --set image.tag=<tag> --set secrets.DB_PASSWD=<passwd> --set mysql.auth.password=<passwd> test ./chart
```

There is a CI/CD process that does this automatically but since the cluster is not publicly accessible, it only performs step 1.
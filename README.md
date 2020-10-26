# SimilarWeb-Hometask
The following was tested on an Ubuntu 18.04 machine.
In order to run the solution you'll have to have
docker-compose & docker installed and run the following command:
`docker-compose up -d `

or run setup_env.sh  to handle docker&docker-compose installations and 
bring up the env with docker-compose.

Loadbalancer:
I've chosen nginx as a loadbalancer since it answers most of the requirments of the task.
this can be accessed by quering http://localhost:8080 after the compose brings everything up.

Service:
To simulate the service i've used flask on python.
the service has 3 methods register,changePassword,and login.
I've built a custom docker based on pytyhon-alpine docker
and included a Dockerfile for the building proccess.

## Section 1 - Get requirment
By default a server is chosen from the backend in a round-robin fashion like requested on section one.

## Section 2 &3 -POST requirments
Used the mirror module of nginx to mirror post requests
In addition POST requests are automaticliy retried once failed.

Couldn't find a reference to the exponential backoff interval,
from what i've read this part is usually performed by the app or some other 
component that is not the load balancer.

## Section 4 -Metrics 
Regarding exposing metrics i've used stub_status,
and in addition i've ran a promehues exporter docker that allows collection of those metrics by a Prometheus server.

## Section 5 -Performance
I've tweaked a few fields to get better performance and couldn't get to the 1000 req per sec for GET.
The main changes were the number of worker_proccesses(determined by the number of available CPUs)
the number of worker_connections (determined by ulimits on the machine).
and buffer related configurations.

To test performance i've used an siege docker 
the command was : 
`docker run --network similarweb_anetwork --rm lopezs/siege -t20s -c1000 http://nginx:8080/login`

Here is the output:
<br> ** SIEGE 4.0.2 </br>
 ** Preparing 1000 concurrent users for battle.\
The server is now under siege...\
Lifting the server siege...\
Transactions:                  15598 hits\
Availability:                 100.00%\
Elapsed time:                  20.06 secs\
Data transferred:               0.03 MB\
Response time:                  0.61 secs\
Transaction rate:             777.57 trans/sec\
Throughput:                     0.00 MB/sec\
Concurrency:                  471.05\
Successful transactions:       15598\
Failed transactions:               0\
Longest transaction:           17.24\
Shortest transaction:           0.00\


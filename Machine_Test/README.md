# Django Machine Test

## Users

1] admin       password: admin

2] Rohit       password: admin

3] Ganesh      password: admin

## Endpoints

1] List of all clients : 

GET:    http://127.0.0.1:8000/clients/

2] Create a new client :

POST : http://127.0.0.1:8000/clients/

3] 
Retrieve info of a client along with projects assigned to its 
users : 

GET : http://127.0.0.1:8000/clients/id/

eg] http://127.0.0.1:8000/clients/4/

4] Update info of a client

Put : http://127.0.0.1:8000/clients/id/

5] Delete a client

Delete : http://127.0.0.1:8000/clients/id/

6] Create a new project

Post :  http://127.0.0.1:8000/clients/:id/projects/

7] List of all projects assigned to the logged-in user

GET : http://127.0.0.1:8000/projects/


## Note for all

when creating a project , it first takes 2 parametes 1. created by and 2. client , now *submit it* and then it will redirect to create the project .Here you can submit the project.


## Screenshots


1]  List of all the clients
![image](https://github.com/Makarand41/Machine-Test/assets/90332486/844cc181-c6b4-4736-a4a4-392e0cd2dad7)


2] Add a client
![image](https://github.com/Makarand41/Machine-Test/assets/90332486/a9cf474d-e7ad-4456-9834-bbe2ab806603)



3] Update a clinet
![image](https://github.com/Makarand41/Machine-Test/assets/90332486/3919f0ca-6f0d-411a-ac1e-7b12444da669)


4] Delete a client
![image](https://github.com/Makarand41/Machine-Test/assets/90332486/4a2196ee-9483-4a6e-9735-3da78d3c29b7)


5] GET /clients/:id  

![image](https://github.com/Makarand41/Machine-Test/assets/90332486/1e16fb4d-11af-4f30-ab4c-4114bafc6fcc)


6] Add project

![image](https://github.com/Makarand41/Machine-Test/assets/90332486/dadd083c-f39c-4d82-81b7-a844d164ee26)

After that it will be redirected to 
![image](https://github.com/Makarand41/Machine-Test/assets/90332486/9bdb94af-e795-4297-8486-15c0f34edf95)



7] List of all projects

![image](https://github.com/Makarand41/Machine-Test/assets/90332486/98ef6d89-964d-4498-b03d-86f69d08c4c1)


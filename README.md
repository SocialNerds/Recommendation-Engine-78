# Recommendation Engine 

A working example of collaborative filtering with Keras and TensorFlow.

# Check the full explanation video (GR)
[![Έχεις E-shop; Φτιάξε Recommendation Engine #78, live](https://img.youtube.com/vi/u_8z2tuPMZ0/0.jpg)](https://youtu.be/u_8z2tuPMZ0)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) installed

Run in root folder,
~~~~
cp .env.example .env
docker-compose build && docker-compose up -d
~~~~

Login to the container,
~~~~
docker exec -it ai /bin/bash -c "TERM=$TERM exec bash"
~~~~

To check it works,
~~~~
python recommend.py
~~~~

You should see, something like,
~~~~
[5.4434] 5
[3.2223] 3
[2.1112] 3
[5.1343] 5
[4.7483] 4
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)
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
[4.543246] 5
[4.5290008] 5
[3.027997] 3
[2.2298465] 3
[2.5590296] 1
[3.7659636] 4
[4.2453494] 4
[4.7732425] 5
[3.818181] 4
[2.692688] 3
[4.2265015] 5
[4.8662224] 5
[4.166681] 5
[4.54121] 4
[2.5106382] 3
[4.4860234] 5
[3.7508686] 5
[4.2168374] 4
[2.9942043] 3
[4.6258173] 5
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)
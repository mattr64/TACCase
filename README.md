# TACCase

I'm trying to create a set of examples on how to use the TAC Case API in a useful way.
networksDBAPI creates a flask API exposed on port 5001. This interfaces with a MongoDB that holds network element information.
The API takes a hostname and returns all the data about that hostname.
This data can then be used in the TAC API to open a case.

There's a bunch of admin scripts:
generate devices: This is obvious, each run it'll generate 500 devices and populate the mongo with it
dbInteract: CLI so you can see device types and list by type
getdeviceDetailsCLI: Accepts hostname as argument and fetches data from Mongo via flask API << This test works
showallDB just dumps the mongo

The rest is WIP, once I get TAC API access I'll get the interaction working between retrieving data from Mongo, passing that to TAC API and then getting a result.

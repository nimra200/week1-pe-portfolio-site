#!/bin/bash
curl --request POST http://nimra-portfolio.duckdns.org:5000/api/timeline_post -d 'name=Nimra&email=nimra.mlh&content=hello world'
curl http://nimra-portfolio.duckdns.org:5000/api/timeline_post

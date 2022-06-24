from urllib import response
from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/proposals/overview")
async def proposals():
    response = requests.get("https://dao.octusbridge.io/v1/proposals/overview") 
    return response.json()

@app.post("/proposals/search")
async def proposals_search(request: Request):
    json1 =await request.json()
    response = requests.post("https://dao.octusbridge.io/v1/proposals/search", json=json1)
    return response.json()

@app.post("/voters/{voter}/search")
async def voter_search(request: Request, voter:str):
    json1 =await request.json()
    response = requests.post("https://dao.octusbridge.io/v1/voters/" + voter + "/search", json=json1)
    return response.json()

@app.post("/voters/proposals/count")
async def count_proposals(request: Request):
    json1 = await request.json()
    response = requests.post("https://dao.octusbridge.io/v1/voters/proposals/count", json=json1)
    return response.json()

@app.post("/voters/proposals/count/search")
async def count_proposals_search(request: Request):
    json1 = await request.json()
    response = requests.post("https://dao.octusbridge.io/v1/voters/proposals/count/search", json=json1)
    return response.json()

@app.post("/votes/search")
async def votes_search(request: Request):
    json1 = await request.json()
    response = requests.post("https://dao.octusbridge.io/v1/votes/search", json=json1)
    return response.json()
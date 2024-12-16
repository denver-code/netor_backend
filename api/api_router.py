from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/")
async def root():
    return {"message": "Hello World"}


from easynetsim import NetworkSimulator
from pydantic import BaseModel
from typing import List, Optional


class Node(BaseModel):
    hostname: str
    ip: str


class Link(BaseModel):
    source: str
    destination: str
    latency: Optional[int] = 20


class SimulationInput(BaseModel):
    nodes: List[Node]
    links: List[Link]


@api_router.post("/simulate")
async def simulate(input: SimulationInput, src_node: str, dst_node: str):
    simulator = NetworkSimulator()
    simulator.load_network(input.model_dump())

    return simulator.ping(src_node, dst_node)

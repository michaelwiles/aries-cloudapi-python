import logging

from fastapi import APIRouter, Depends
from aries_cloudcontroller import AriesAgentControllerBase

from dependencies import member_agent

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/generic/connections", tags=["connections"])


@router.get("/create-invite", tags=["connections", "create"])
async def create_invite(
    aries_controller: AriesAgentControllerBase = Depends(member_agent),
):
    invite = await aries_controller.connections.create_invitation()
    return invite


@router.get("/accept-invite", tags=["connections", "accept"])
async def accept_invite(
    invite: dict,
    aries_controller: AriesAgentControllerBase = Depends(member_agent),
):
    accept_invite_res = await aries_controller.connections.accept_connection(invite)
    return accept_invite_res


@router.get("/", tags=["connections"])
async def get_connections(
    aries_controller: AriesAgentControllerBase = Depends(member_agent),
):
    connections = await aries_controller.connections.get_connections()
    return connections


@router.get("/{conn_id}", tags=["connections"])
async def get_connection_by_id(
    connection_id: str,
    aries_controller: AriesAgentControllerBase = Depends(member_agent),
):
    connection = await aries_controller.connections.get_connection(connection_id)
    return connection


@router.delete("/{conn_id}", tags=["connections"])
async def delete_connection_by_id(
    connection_id: str,
    aries_controller: AriesAgentControllerBase = Depends(member_agent),
):
    remove_res = await aries_controller.connections.remove_connection(connection_id)
    return remove_res
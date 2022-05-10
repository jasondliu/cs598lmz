import weakref
import logging
import datetime

import sqlalchemy
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker

from vj4 import db
from vj4.model import builtin
from vj4.model import base
from vj4.model import domain
from vj4.model import user
from vj4.model import document
from vj4.model.adaptor import discussion

_logger = logging.getLogger(__name__)

DocumentRecord = document.get_document_record('discussion')


async def get_discussion_count(domain_id, *, conn=None):
  if conn is None:
    async with db.Connection.acquire() as conn:
      return await get_discussion_count(domain_id, conn=conn)
  return await conn.scalar(DocumentRecord.select('count(*)').where(
    DocumentRecord.domain_id == domain_id))

async def add_discussion(domain_id, uid, title, content, *, conn=None):
  if conn

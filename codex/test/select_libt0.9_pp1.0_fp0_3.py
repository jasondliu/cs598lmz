import selectors

from libs.config import CONF
from data.search_parse_website import parse_website
from data.search_parse_novel import parser_novel
from libs.book_queue import BookEventQueue, BookEvent
from base.base_logger import logger
from libs.config import BOOK_TABLES
from run import app


@app.task(name="task.get_book.start", ignore_result=True)
def start():
    # 实例化一个事件队列对象
    book_event_queue = BookEventQueue()
    # 创建一个selectors对象
    sel = selectors.DefaultSelector()
    # 注册队列读取事件
    sel.register(book_event_queue, selectors.EVENT_READ, data=book_search)

    logger.info(f"Start task to get book url.")

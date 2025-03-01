from aiogram import Router

from .messages import on as messages_router
from .modes.dialog_with_ai import on as dialog_with_ai_router
from .modes.pronunciation_check import on as pronunciation_check_router
from .modes.translate_practice import on as translate_practice
from .start_menu import on as start_menu_router

main_router = Router()
main_router.include_routers(
    start_menu_router,
    pronunciation_check_router,
    dialog_with_ai_router,
    translate_practice,
    messages_router,
)

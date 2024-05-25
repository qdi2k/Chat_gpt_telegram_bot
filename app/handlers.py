from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.generators import gpt4
from app.logger import log

router = Router()


class Generate(StatesGroup):
    text = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    log(f'username: @{message.from_user.username} - '
        f'id: {message.from_user.id} \n'
        f' Input: {message.text}')
    await message.answer('Добро пожаловать! Напишиите ваш запрос')
    await state.clear()


@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer('Подождите, ваше сообщение генерируется...')


@router.message(F.text)
async def generate(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4(message.text)
    log(f'username: @{message.from_user.username} - '
        f'id: {message.from_user.id} \n'
        f' Input: {message.text}')
    await message.answer(response.choices[0].message.content)
    await state.clear()

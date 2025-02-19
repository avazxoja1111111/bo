# Botni yaratish
from bot import TOKEN


bot = Bot(token=TOKEN, default=parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
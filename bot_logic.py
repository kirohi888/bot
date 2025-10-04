import random

def gen_sticker():
    stickers = ['CAACAgUAAxkBAAEPfu1o4MpQMQSTEB_KYhKRTQgYBWh7pQACOREAAsKgEFZSuzxu0IndCDYE', 'CAACAgUAAxkBAAEPfvRo4M-prgEC7dJ3jG8goiwUiDkAAV8AAlYUAAJnWihUBdXv4UvvG1w2BA', \
                'CAACAgUAAxkBAAEPfvZo4M_J11JSYllWIJ2k6DhJCodYTAACKBQAArjEKFSHDmJRUe5yODYE', 'CAACAgIAAxkBAAEPfvpo4NCSGIMiIUZTgD87zNipi9NCzwAC2xYAAo1pAAFIPRpJ-1XJxcA2BA', \
                'CAACAgIAAxkBAAEPfvxo4NCrbZBP0MsDCLCz0KTmf-IniwACgz0AArf4IEsHy7ZhpJnsgzYE', 'CAACAgIAAxkBAAEPfv5o4NDPmtAqY80JbhtFNovasCxvEQACrDIAAuPvIEsM_BZUzmYYyjYE', \
                'CAACAgIAAxkBAAEPfwABaODRG3bAgQq8Zoq1sc1t-FGnGN4AAuIRAAKMLf0HrkE15dSHMg82BA', 'CAACAgUAAxkBAAEPfwJo4NFSwnvaIuFMf3-MuKqAC5JmYgACbREAAk5rsFdogPSpDPdldDYE', \
                'CAACAgUAAxkBAAEPfwRo4NFzhcYmnljCY1us3LU-hndBhgACORAAAreRAAFWsiQa1EVGHck2BA', 'CAACAgIAAxkBAAEPfwxo4NWvwjTdyiQOrLkaNxLXaTy9cwACkjYAAv0LwEhE2Qs2zjI4GzYE', \
                'CAACAgIAAxkBAAEPfw5o4NXhd6OYL3krZAXYsiEtx8g0owACYzoAAg5JuUiqScsQLr79OTYE', 'CAACAgIAAxkBAAEPfxBo4Na3eN2SLYRZQ7VuuhuQxlr7sQAC2VsAArhR4UkIKQmxJf61BTYE', \
                'CAACAgQAAxkBAAEPfxJo4NbnfhNR-7SlULnE_kInJMJ9zgACNw0AAnVh8VEZ5rHvQTIr7DYE', 'CAACAgIAAxkBAAEPfxRo4NcB9ZaivIujJwABllspWQw_ZXwAApseAAKh_IBI-RtoUDk685s2BA', \
                'CAACAgIAAxkBAAEPfxZo4NcVKC0YJRLDZvameZbLYQfAVAAC_EwAAoEESUofB-zLUAnsSjYE', 'CAACAgIAAxkBAAEPfxho4Newyt7KhT-ypX59unh02CFfYAAC9jUAAkQbAUs93Tpt6mQebzYE', \
                'CAACAgUAAxkBAAEPfxpo4Nn9T-uVx_js9WhBbqfrGbnQCwACbgoAAhmc4Fdb9S1FNva8NjYE', 'CAACAgIAAxkBAAEPfxxo4NvVdwFawReoPtgij4lwCwrJTgAClXgAAlD7iUlQXacy1fO5tzYE', \
                'CAACAgUAAxkBAAEPfx5o4NxGQsQZSWmapxG8sg7GZt0lBQACqyUAAqDoOVTIj91DF-IjqjYE']
    return random.choice(stickers)

def gen_pass(password_len):
    symbol = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''

    for i in range(password_len):
        password += random.choice(symbol)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

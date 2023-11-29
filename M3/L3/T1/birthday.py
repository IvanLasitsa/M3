
def season(m):
    if m < 3:
        return "зима"
    else:
        if m < 6:
            return "весна"
        else:
            if m < 9:
                return "літо"
            else:
                if m < 12:
                    return "осінь"
                else:
                    return "зима"

# Функція повертає рядок з назвою дня тижня, коли народилася людина


def day(d):
    if d == 1:
        return "понеділок"
    if d == 2:
        return "вівторок"
    if d == 3:
        return "середа"
    if d == 4:
        return "четвер"
    if d == 5:
        return "п'ятниця"
    if d == 6:
        return "субота"
    return "неділя"

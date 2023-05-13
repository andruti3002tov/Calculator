<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/styles/styles.css">
    <meta charset="UTF-8">
    <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png">
    <title>Калькулятор</title>
</head>
<body class="body">
    <form method="post" action="/">
        <div class="main">
            <input class="field" type="text" name="first" placeholder="Введите первое число"><br>
            <input class="field" type="text" name="second" placeholder="Введите второе число"><br>
            <div class="result">
                <a> Ответ: {{result}}</a><br>
            </div>
            <button type="submit" value='+' class="button" name="sum"> + </button>
            <button type="submit" value="-" class="button" name="minus"> - </button>
            <button type="submit" value=":" class="button" name="division"> / </button>
            <button type="submit" value="*" class="button" name="multi"> * </button>
        </div>
    </form>
</body>
</html>
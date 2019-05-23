<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="/static/login/main.css">
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,800|Ultra&display=swap" rel="stylesheet"> 
</head>
<body>
    <a href="/"><img class="logo" src="/static/LPD_logo.png" alt="LPD_logo"></a>
    <header class="header">
        <h1>LOLI POLICE DEPARTMENT</h1>
        <h2>TO SERVE THE SMALLEST</h2>
    </header>
    <hr>
    % if logout_btn is True:
        <a class="logout_btn" href="/logout">Logout</a>
    % end
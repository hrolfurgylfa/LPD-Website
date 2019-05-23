% include("logged_in/parts/header.tpl", title="LPD login", logout_btn=False)
<main class="login_box">
    <section class="window_bar">LPD - Suspect Database</section>
    <form action="/get_cookie" method="post" class="login_fields">
        <p class="login_text">Please login below to access this LPD computer.</p>
        <p class="input_text">Password:</p>
        <input name="password" type="password">
        <br>
        <input class="login_btn" type="submit" value="login">
    </form>
</main>
% include("logged_in/parts/footer.tpl")
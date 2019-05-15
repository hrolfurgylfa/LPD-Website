<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Officer Index</title>
    <link rel="stylesheet" href="/static/officer_index/main.css">
</head>
<body>
    <h1>Officer Index</h1>
    <table class="table sortable">
        <tr>
            <th>Disord username</th>
            <th>VRChat username</th>
            <th>Time Zone</th>
            <th>LPD Join Date</th>
            <th>Rank</th>
            <th>Gear</th>
        </tr>
        % for officer in officer_index:
            <!-- <p>{{ officer }}</p> -->
            <tr>
                <td>{{ officer[0] }}</td>
                <td>{{ officer[1] }}</td>
                <td>{{ officer[2] }}</td>
                <td>{{ officer[3] }}</td>
                <td>{{ officer[4] }}</td>
                <td>{{ officer[5] }}</td>
            </tr>
        % end
    </table>
    <script src="/static/officer_index/sorttable.js"></script>
    <script src="/static/officer_index/main.js"></script>
</body>
</html>
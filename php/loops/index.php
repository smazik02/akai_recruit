<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Loops</title>
</head>

<body>
    <?php
    $end = "";
    for ($x = 100; $x >= 0; $x--) {
        $num = "";
        if ($x == 0) {
            $num = 0;
        } else {
            if ($x % 4 == 0) {
                $num = "Fire <br>";
            } else if ($x % 7 == 0) {
                $num = "Boom <br>";
            } else {
                $num = "$x <br>";
            }
            if ($x % 10 == 0) {
                $num = '<span style="color:red">' . $num . '</span>';
                $num = str_repeat($num, 10);
            }
        }
        $end .= $num;
    }
    echo "$end";
    ?>
</body>

</html>
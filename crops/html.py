template1 = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey;
     background-color:rgba(255, 255, 255, 0.8);border-radius:6px;
      padding: 10px; font-size:14px; right: 70px; bottom: 180px;'>
<div class='legend-title'>Legend </div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style=’background:#ffffff;opacity:0.6;’></span>0</li>
    <li><span style='background:#ffffb2;opacity:0.6;'></span>1 - """
minitemp1 = """</li>
    <li><span style='background:#fecc5c;opacity:0.6;'></span>"""
minitemp2 = """</li>
    <li><span style='background:#fd8d3c;opacity:0.6;'></span>"""
minitemp3 = """</li>
    <li><span style='background:#f03b20;opacity:0.6;'></span>"""
minitemp4 = """</li>
    <li><span style='background:#bd0026;opacity:0.6;'></span>"""
template2 = """</li>
  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""
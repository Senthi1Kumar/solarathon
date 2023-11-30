import solara


@solara.component
def Page():
    html = """
<!DOCTYPE html>
<html>
<head>
<title>Heart rate</title>  
<style>
body {
  background-color: #F2F2F2;
  font-family: Arial; 
}

.header {
  padding: 40px;
  text-align: center;
  background-image: linear-gradient(to bottom right, #4D77FF, #eedebe); 
  color: white; 
  font-size: 32px;  
}

.intro {
  max-width: 700px;
  margin: auto;
  padding: 30px; 
}

</style>
</head>
<body>
  <div class="header">
    Heart rate
  </div>

  <div class="intro">
    <h2>Your sleep companion</h2> 
    SleepHealth helps you log, analyze and enhance your sleep through actionable insights.
  </div>
</body>
</html>
"""
    with solara.VBox() as main:
        solara.HTML(tag="div", style=['body','.header','.intro'],unsafe_innerHTML=html)
        return main
    
# @solara.component
# def Layout(children):
#     return solara.AppLayout(children=children)

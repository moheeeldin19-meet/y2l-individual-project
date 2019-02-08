Feel free to delete/rename this file and add more .js files in this folder.
	mixin triangle(num, color)
    polygon( 
    points=""
    fill="none" 
    stroke=color 
    stroke-width="5")
    animate(
      attributeName="points"
      repeatCount="indefinite"
      dur="4s"
      begin=num+"s"
      from="50 57.5, 50 57.5, 50 57.5"
      to="50 -75, 175 126, -75 126")

//- Create Overlay  
div(class="overlay")

//- Instantiate triangles
div(class="container")
  - for (var x = 1; x < 60; x++)
    svg(class="shape" viewBox="0 0 100 115" preserveAspectRatio="xMidYMin slice")
      +triangle(0, "hsl(42, 100%, 53%)")
      +triangle(1, "hsl(49, 97%, 54%)")
      +triangle(2, "hsl(48, 7%, 87%)")
      +triangle(3,"hsl(60, 100%, 47%)")
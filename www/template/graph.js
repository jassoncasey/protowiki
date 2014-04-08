<script type="text/javascript">

var w = 300;
var h = 300;

var svg = d3.select("body")
  .append("svg")
  .attr("width", w)
  .attr("height", h);

d3.json("flare.json", function(root) {

  var force = d3.layout.force()
    .nodes(root.nodes)
    .links(root.edges)
    .linkDistance([50])
    .charge([-200])
    .size([w, h])
    .start();

  var edges = svg.selectAll("line")
    .data(root.edges)
    .enter()
    .append("line")
    .style("stroke", "#000000")
    .style("stroke-width", 1);

  var nodes = svg.selectAll("circle")
    .data(root.nodes)
    .enter()
    .append("circle")
    .attr("r", 10)
    .style("fill", function(d, i) {
      return "#ffaa00"; //colors(i);
    })
    .call(force.drag);

  force.on("tick", function() {
    edges.attr("x1", function(d) { return d.source.x; })
      .attr("x2", function(d) { return d.source.y; })
      .attr("y1", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });
    nodes.attr("cx", function(d) { return d.x; } )
      .attr("cy", function(d) { return d.y; } );
  });

});
  
</script>

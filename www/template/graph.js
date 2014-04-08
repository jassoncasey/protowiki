<script type="text/javascript">

var jq_view = $("#prime_view");
var width = jq_view.width();
var height = 800;

var view = d3.select("#prime_view");
var svg = view.append("svg")
  .attr("width", width)
  .attr("height", height);

d3.json("flare.json", function(root) {

  var force = d3.layout.force()
    .nodes(root.nodes)
    .charge([-2000])
    .size([width,height])
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
    .attr("r", 30)
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

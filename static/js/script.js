function initialize() {
	container = document.getElementById("container");
}

function addRow() {
	var row = container.insertRow(-1);
	
	for (var i = 0; i < 4; i++) {
		var col = row.insertCell(-1);
		var box = document.createElement("div");
		box.className = "white";
		box.addEventListener("click", function() {
			if (this.className == "white")
				this.className = "black";
			else if (this.className == "black")
				this.className = "red";
			else if (this.className == "red")
				this.className = "blue";
			else if (this.className == "blue")
				this.className = "green";
			else if (this.className == "green")
				this.className = "yellow";
			else if (this.className == "yellow")
				this.className = "white";
		});
		col.appendChild(box);
	}
	
	var blackInput = document.createElement("input");
	blackInput.className = "black_input";
	blackInput.type = "number";
	blackInput.defaultValue = 0;
	var col2 = row.insertCell(-1);
	col2.appendChild(blackInput);
	
	var whiteInput = document.createElement("input");
	whiteInput.className = "white_input";
	whiteInput.type = "number";
	whiteInput.defaultValue = 0;
	var col3 = row.insertCell(-1);
	col3.appendChild(whiteInput);
	
}
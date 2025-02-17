# os-producer-consumer-lab
In this lab you will create a bounded buffer, producer and consumer in Python to model the producer-consumer relationship and mimic the issues with a bounded buffer. You may collaborate with others on this lab.

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name prod_cons_buff python=3.13.1</li>
		<li>conda activate prod_cons_buff</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the prod_cons_buff anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
   <li><b>Buffer class</li></b></li>
    <ol>
      <li>The buffer class will represent the bounded buffer</li>
      <li>__init__ should take in size as a parameter</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>size: size of the buffer</li>
          <li>items: list to store items in the buffer.</li>
          <li>in_pointer: initialize to 0</li>
          <li>out_pointer: initialize to 0</li></ol>
      <li><b>Methods</b></li>
        <ol>
          <li>increment_in: increments the in pointer</li>
          <li>increment_out: increments the out pointer</li>
          <li>is_empty: determines if the buffer is empty. Returns True or False</li>
          <li>is_full: determines if the buffer is full. Returns True or False</li>
        </ol>
      </ol>
  <br>
  <li><b>Producer class</b></li>
    <ol>
      <li>The producer will produce processes represented as integers to add to the buffer</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>None</li>
        </ol>
    <li><b>Methods</b></li>
      <ol>
        <li>produce: Generates a random number between 0 and 100 and adds to buffer.</li>
	<li>Constraint: Remember, the producer can't add items to the buffer if the buffer is full.</li>
      </ol>
  </ol>
  <br>
  <li><b>Consumer class</b></li>
    <ol>
      <li>The condumer will consume processes from the buffer</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>None</li>
        </ol>
      <li><b>Methods</b></li>
        <ol>
          <li>consume: Consumes and returns an item from the buffer.</li>
	<li>Constraint: Remember, the consumer can't consume any items if there are no items in the buffer.</li>
        </ol>
    </ol>


## Hints
<ol>
	<li>You will probably need the random module.</li>
	<li>The size of the buffer should not change while producing and consuming.</li>
</ol>

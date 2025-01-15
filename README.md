# os-producer-consumer-lab
In this lab you will create a bounded buffer, producer and consumer in Python to model the producer-consumer relationship.

## Set Up
Create new anaconda environment using these commands
	conda create –name prod_cons_buff python=3.13.1

Pull starter code from GitHub classroom

Open in VS code and switch to the prod_cons_buff anaconda environment

## Instructions
<ol>
   <li><b>Buffer class</li></b></li>
    <ol>
      <li>The buffer class will represent the bounded buffer</li>
      <li>__init__ should take in size as a parameter</li>
      <li><b>Attributes</b></li>
        <ol>
          <li>size: size of the buffer</li>
          <li>items: list to store items in the buffer</li>
          <li>in_pointer:</li>
          <li>out_pointer:</li></ol>
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
        </ol>
    </ol>


## Hints
You will probably need the random and time modules.

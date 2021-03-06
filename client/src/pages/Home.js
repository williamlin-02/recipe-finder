import { useState } from 'react';

async function filterRecipes(params){
	return fetch('/127.0.0.1:5000/recipe/filter',{
		method: 'GET',
		headers: {
		     'Content-Type': 'application/json'
		},
		body: JSON.stringify(params)
	}).then(data => data.json())
}

const Home = () =>{
	const [search_input, setSearchInput] = useState('')

	const handleSubmit = async e => {
		e.preventDefault();

	}

	return(
	<div class="s013">
      <form>
        <fieldset>
          <legend>QUICK FIND YOUR CITY</legend>
        </fieldset>
        <div class="inner-form">
          <div class="left">
            <div class="input-wrap first">
              <div class="input-field first">
                <label>WHAT</label>
                <input type="text" placeholder="ex: food, service, bar, hotel" />
              </div>
            </div>
            <div class="input-wrap second">
              <div class="input-field second">
                <label>WHERE</label>
                <div class="input-select">
                  <select data-trigger="" name="choices-single-defaul">
                    <option placeholder="">1 adult</option>
                    <option>2 adults</option>
                    <option>3 adults</option>
                    <option>4 adults</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <button class="btn-search" type="button">SEARCH</button>
        </div>
      </form>
    </div>
		)
}

export default Home;
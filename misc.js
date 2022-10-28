import './App.css';
import {useState} from "react";

function App() {
  const [category , setCategory] = useState([{title:'Нажми кнопку категории'}])
  const [services , setServices] = useState( [{title:'Нажми кнопку сервисы'}])

  function get_categories(){
    fetch('http://127.0.0.1:8000/api1/v1/categoryes/')
        .then(response=>response.json())
        .then(categories=>{
            console.log(categories)
            setCategory(categories)
        })
  }
  function get_services(){
        fetch('http://127.0.0.1:8000/api1/v1/service/')
        .then(response=>response.json())
        .then(services=>{
            console.log(services)
            setServices(services)
        })
  }
  // console.log(category)
  // console.log(services)
  return (
      <>
        <div className="App">
            <h1>Hello Nick</h1>
            <input type={"button"} value={'Получить категории'} onClick={get_categories}/>
            <input type="button" value={'Получить сервисы'} onClick={get_services}/>
        </div>
        <div className="wrapper">
            <div className="categ">
                {category.map(item=>item.title)}
            </div>
            <div className="serv">
                {services.map(item=>item.title)}
            </div>
    </div>
    </>
  );
}

export default App;
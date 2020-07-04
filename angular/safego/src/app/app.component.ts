import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import {HttpClient} from '@angular/common/http';

declare let leaflet_map:any;

@Component({
  selector: 'app-root',
  template: '<question-form></question-form>'
})

export class AppComponent{
  title = 'safego';

  constructor(private http:HttpClient) { }

  onAddressSubmit(addressForm:any){
    var url='http://localhost:8000/riskIndex/';
    console.log(addressForm);
    var data = addressForm;
    this.http.post(url, data).subscribe(function(response){
      console.log(response)
    })
  }
}
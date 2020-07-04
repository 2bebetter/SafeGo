import { Component } from '@angular/core';
import { Address } from './address';
import {HttpClient} from '@angular/common/http';
 
@Component({
    selector: 'address-form',
    templateUrl: 'address-form.component.html'
})
export class AddressFormComponent {
  constructor(private http:HttpClient) { }
  model = new Address(1, '天安门广场', '北京');
  submitted = false;
  onSubmit() { 
    this.submitted = true; 
  }
  get diagnostic() { 
    return JSON.stringify(this.model); 
  }
  active = true;
  onAddressSubmit(addressForm:any){
    var url='http://localhost:8000/search_risk/';
    //console.log(addressForm);
    var data = addressForm.value;
    data = this.http.post(url, data).subscribe(response => {
      alert(response['message']);
    });
  }
}
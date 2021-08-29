import datetime
from typing import Literal, Union

Color = Literal[ 'red', 'blue', 'green', 'purple', 'orange', 'midnight_blue', 'coffee', 'burgundy', 'wintergreen']

class NumericsIo():
    def __init__(self):
        pass

    def convert_numerics_array(self, data: Union[list, dict], is_hour_dencity_list: bool=False, is_day_dencity_dict: bool=False) -> dict:
        result = []
        if type (data) is list:
            i = 0
            for item in data:
                if type(item) is int or type(item) is float:
                    if is_hour_dencity_list is False:
                        result.append( { 'value': item } )
                    else:
                        result.append( { 'hour': i, 'value': item } )
                        i+=1
        elif type (data) is dict:
            for key, value in data.items():
                if type(value) is int or type(value) is float:
                    if is_day_dencity_dict is False:
                        result.append( { 'name': key, 'value': value } )
                    else:
                        result.append( { 'date': key, 'value': value } )
        else :
            raise Exception('Unknown data type:' + str(type(data)))
        return result

    def get_label(self, postfix: str, data: str, color: Color=None) -> str:
        return {
            'postfix': postfix,
            'color': color,
            'data': {
                'value': data
            }
        };

    def get_number(self, postfix: str, data: Union[int, float], color: Color=None):
        return {
            'postfix': postfix,
            'color': color,
            'data': {
                'value': data
            }
        };

    def get_count_and_difference_indicator(self, postfix: str, data1: Union[int, float], data2: Union[int, float], color: Color=None):
        return {
            'postfix': postfix,
            'data':[
                {
                    'value': data1,
                },
                {
                    'value': data2,
                }
            ],
            'color': color
        };

    def line_graph(self, postfix: str, data: list, color: Color=None):
        return {
            'postfix': postfix,
            'data': self.convert_numerics_array(data),
            'color': color
        };

    def get_named_line_graph(self, postfix: str, data: list, color: Color=None):
        return {
            'postfix': postfix,
            'data': self.convert_numerics_array(data),
            'color': color
        };

    def get_pie_chart(self, data: dict, color: Color=None):
        return {
            'data': self.convert_numerics_array(data),
            'color': color
        };

    def get_top_list_funnel_chart(self, data: dict, value_name_header: str, value_header: str, color: Color=None):
        return {
            'value_name_header': value_name_header,
            'value_header': value_header,
            'data': self.convert_numerics_array(data),
            'color': color
        };

    def get_gauge(self, postfix: str, value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float], color: Color=None):
        return {
            'postfix': postfix,
            'data': {
                'minValue': min_value,
                'value': value,
                'maxValue': max_value
            },
            'color': color,
        };

    def get_timer(self, name: str, date_value: datetime, color: Color=None):
        return {
            'data': {
                'name': name,
                'dateValue': date_value.isoformat(),
                'dateFormat': "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"
            },
            'color': color
        };

    def get_hour_density_chart(self, postfix: str, data: list, color: Color=None):
        return {
            'postfix': postfix,
            'data': self.convert_numerics_array(data, is_hour_dencity_list=True),
            'color': color
        };

    def get_day_density_chart(self, postfix: str, data: dict, color: Color=None):
        return {
            'postfix': postfix,
            'data': self.convert_numerics_array(data, is_day_dencity_dict=True),
            'color': color
        };

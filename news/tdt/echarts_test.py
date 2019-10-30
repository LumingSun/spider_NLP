from pyecharts import Line, Page, Style
from data_process import get_matrix
import numpy as np
def create_charts(attr,matrix):
        page = Page()
        style = Style(
        width=1200, height=600
        )
        # attr = ['1.1', '1.2', '1.3', '周四', '周五', '周六', '周日']
        chart = Line("政治话题热度趋势", **style.init_style)
        topic_list = ['国内政治','主权','台湾问题','香港','人权','西藏问题','朝鲜','军事','安全','经济','股市','农业',\
                      '民生','教育','宗教','交通','环境','法律','医疗']
        for i in range(7):
            chart.add(topic_list[i], attr, matrix[i].tolist(),line_width=4,line_curve=1,legend_selectedmode='multiple',
                      tooltip_tragger='axis',mark_point=["max"])

        page.add(chart)

        chart = Line("军事话题热度趋势", **style.init_style)
        topic_list = ['国内政治', '主权', '台湾问题', '香港', '人权', '西藏问题', '朝鲜', '军事', '安全', '经济', '股市', '农业', \
                      '民生', '教育', '宗教', '交通', '环境', '法律', '医疗']
        for i in range(7, 9):
            chart.add(topic_list[i], attr, matrix[i].tolist(), line_width=4, line_curve=1,
                      legend_selectedmode='multiple',
                      tooltip_tragger='axis', mark_point=["max"])
        page.add(chart)

        chart = Line("经济话题热度趋势", **style.init_style)
        topic_list = ['国内政治', '主权', '台湾问题', '香港', '人权', '西藏问题', '朝鲜', '军事', '安全', '经济', '股市', '农业', \
                      '民生', '教育', '宗教', '交通', '环境', '法律', '医疗']
        for i in range(9, 11):
            chart.add(topic_list[i], attr, matrix[i].tolist(), line_width=4, line_curve=1,
                      legend_selectedmode='multiple',
                      tooltip_tragger='axis', mark_point=["max"])
        page.add(chart)

        chart = Line("社会话题热度趋势", **style.init_style)
        topic_list = ['国内政治', '主权', '台湾问题', '香港', '人权', '西藏问题', '朝鲜', '军事', '安全', '经济', '股市', '农业', \
                      '民生', '教育', '宗教', '交通', '环境', '法律', '医疗']
        for i in range(11, 19):
            chart.add(topic_list[i], attr, matrix[i].tolist(), line_width=4, line_curve=1,
                      legend_selectedmode='multiple',
                      tooltip_tragger='axis', mark_point=["max"])
        page.add(chart)

        return page


data_list ,matrix = get_matrix()
create_charts(data_list,matrix).render()
# create_charts().render()

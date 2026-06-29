# 深圳出租车数据分析平台

基于 Apache Spark 清洗深圳市出租车乘车出行数据，使用 Flask + ECharts + Leaflet 构建的可视化分析平台。

## 技术栈

- **数据处理**: Apache Spark (PySpark) 3.5.2
- **后端**: Flask 3.0 (Python 3.8)
- **前端图表**: ECharts 5.4
- **地图可视化**: Leaflet.js + Leaflet.heat
- **数据源**: 深圳市出租车轨迹数据（160万条记录，500辆车）

## 项目结构

taxi_viz/
├── app.py                  # Flask 后端
├── templates/index.html    # 前端页面
├── static/
│   ├── js/main.js         # 核心 JS（数据+图表+地图）
│   └── css/style.css      # 样式
└── data/                   # Spark 聚合数据（JSON）
    ├── summary.json        # 总览统计
    ├── speed_dist.json     # 速度分布
    ├── time_dist.json      # 时段分布
    ├── hourly_status.json  # 24小时载客状态
    ├── cross.json          # 载客状态×速度交叉
    ├── top_vehicles.json   # Top10 车辆
    ├── gps_heatmap.json    # GPS 热力图采样点
    ├── hourly_data.json    # 逐小时 GPS 采样
    └── gps_bounds.json     # 深圳地图边界

## 功能模块

| 模块 | 说明 |
|------|------|
| 数据总览 | 4个指标卡 + 4个ECharts图表（速度分布、时段饼图、24h趋势、载客堆叠） |
| 时间滑块 | 顶部时间轴，拖动选择时段，所有图表联动更新 |
| 热力图 | Leaflet + heat.js 实现的 GPS 密度热力图 |
| 交互地图 | Leaflet 地图，鼠标悬停显示经纬度 |
| 车辆排行 | Top10 车辆数据排名 |

## 部署运行

\\\ash
# 安装依赖
pip install flask

# 启动服务
python app.py

# 访问地址
http://127.0.0.1:5000
\\\

## 数据清洗

数据清洗使用 PySpark 在 Hadoop 集群上执行，清洗脚本在 E:\\\\shixun\\\\taxi_clean_spark.py

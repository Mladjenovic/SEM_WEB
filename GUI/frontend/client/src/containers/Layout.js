import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { Nav, Navbar, Container, Row } from "react-bootstrap";

import { Layout, Menu, Breadcrumb } from "antd";
import { RightCircleOutlined } from "@ant-design/icons";

import Query1 from "../screens/Query1.js";
import Query2 from "../screens/Query2.js";

const { Header, Content, Footer, Sider } = Layout;
const { SubMenu } = Menu;

function CustomLayout() {
  const [collapsed, setCollapsed] = useState(false);

  const onCollapse = (collapsed) => {
    setCollapsed(collapsed);
  };

  useEffect(() => {}, []);

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider collapsible collapsed={collapsed} onCollapse={onCollapse}>
        <div className="logo" />
        <Menu theme="dark" defaultSelectedKeys={["1"]} mode="inline">
          <Menu.Item key="1" icon={<RightCircleOutlined />}>
            <Link to="/query1">Query one</Link>
          </Menu.Item>
          <Menu.Item key="2" icon={<RightCircleOutlined />}>
            <Link to="/query2">Query two</Link>
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 0 }} />
        <Content style={{ margin: "0 16px" }}>
          <div
            className="site-layout-background"
            style={{ padding: 24, minHeight: 360 }}
          >
            <Routes>
              <Route exact path="/query1" element={<Query1 />}></Route>
            </Routes>
            <Routes>
              <Route exact path="/query2" element={<Query2 />}></Route>
            </Routes>
          </div>
        </Content>
        <Footer style={{ textAlign: "center" }}>Semantic web ontology</Footer>
      </Layout>
    </Layout>
  );
}

export default CustomLayout;

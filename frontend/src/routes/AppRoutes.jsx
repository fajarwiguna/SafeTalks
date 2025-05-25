import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Welcome from '../pages/Welcome';
import Login from '../pages/Login';
import Signup from '../pages/Signup';
import ForgotPassword from '../pages/ForgotPassword';
import VerifyCode from '../pages/VerifyCode';
import Dashboard from '../pages/Dashboard';
import RoomChat from '../pages/RoomChat';
import Profile from '../pages/Profile';
import EditProfile from '../pages/EditProfile';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Welcome />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/verify-code" element={<VerifyCode />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/room-chat" element={<RoomChat />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/account/edit" element={<EditProfile />} />
    </Routes>
  );
};

export default AppRoutes;

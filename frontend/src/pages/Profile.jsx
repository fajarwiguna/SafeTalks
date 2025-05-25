import React from 'react';
import '../styles/style.css';
import { useNavigate } from 'react-router-dom';
import { FaArrowLeft, FaEnvelope } from 'react-icons/fa';

const Profile = () => {
  const navigate = useNavigate();

  return (
    <div className="profile-container">
      {/* Header */}
      <div className="profile-header">
        <button className="back-button" onClick={() => navigate('/dashboard')}>
          <FaArrowLeft />
        </button>
      </div>

      {/* Profile card */}
      <div className="profile-card">
        {/* Top Section */}
        <div className="profile-top">
          <div className="profile-avatar-wrapper">
            <img
              src="https://cdn-icons-png.flaticon.com/512/4140/4140048.png"
              alt="avatar"
              className="profile-avatar"
            />
            <div className="profile-info">
              <h3 className="profile-name">brooo</h3>
              <p className="profile-email">brooowww@gmail.com</p>
            </div>
          </div>
          <button className="edit-button">Edit</button>
        </div>

        {/* Form fields */}
        <div className="profile-form">
          <div className="form-row">
            <div className="form-group">
              <label>Nick Name</label>
              <input type="text" placeholder="Your Nick Name"/>
            </div>
            <div className="form-group">
              <label>Gender</label>
              <select>
                <option>Select</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
              </select>
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Time Zone</label>
              <select>
                <option>Select</option>
                <option>UTC+0</option>
                <option>UTC+7</option>
                <option>UTC+8</option>
                <option>UTC+9</option>
              </select>
            </div>
            <div className="form-group">
              <label>Country</label>
              <select>
                <option>Select</option>
                <option>Indonesia</option>
                <option>USA</option>
                <option>Japan</option>
                <option>UK</option>
              </select>
            </div>
          </div>

          {/* Email Display */}
          <div className="email-section">
            <h4>My email Address</h4>
            <div className="email-box">
              <FaEnvelope className="email-icon" />
              <div>
                <p className="email-address">brooowww@gmail.com</p>
                <p className="email-date">1 month ago</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;